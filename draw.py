#!/usr/bin/env python3
"""Draw the front page of THE WORLD TODAY for Thursday 26 November 2026.

Build-time only: renders entry.png (1024x1024) from the six verified stories
of 26 November 2026 plus a footer ticker. Pure Pillow, no network.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 64, 120)
GREY = (90, 86, 76)
RULE = (40, 40, 40)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, width, text, fnt, fill=INK, leading=None):
    leading = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color=RED):
    f = SANS_B(17)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return y + 24


def headline(draw, x, y, width, text, size=34):
    f = SERIF_B(size)
    y2 = para(draw, x, y, width, text, f, leading=int(size * 1.08))
    return y2


def hline(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def vline(draw, x, y0, y1, width=1, fill=(150, 145, 130)):
    draw.line([(x, y0), (x, y1)], fill=fill, width=width)


# ---- simple flat icons -------------------------------------------------
def icon_rocket(d, cx, cy, s, color=BLUE):
    # body
    d.polygon([(cx, cy - s), (cx + s * 0.42, cy - s * 0.1), (cx + s * 0.42, cy + s * 0.5),
               (cx - s * 0.42, cy + s * 0.5), (cx - s * 0.42, cy - s * 0.1)], fill=color)
    # window
    d.ellipse([cx - s * 0.16, cy - s * 0.28, cx + s * 0.16, cy + s * 0.04], fill=PAPER)
    # fins
    d.polygon([(cx - s * 0.42, cy + s * 0.3), (cx - s * 0.75, cy + s * 0.75), (cx - s * 0.42, cy + s * 0.55)], fill=color)
    d.polygon([(cx + s * 0.42, cy + s * 0.3), (cx + s * 0.75, cy + s * 0.75), (cx + s * 0.42, cy + s * 0.55)], fill=color)
    # flame
    d.polygon([(cx - s * 0.18, cy + s * 0.55), (cx + s * 0.18, cy + s * 0.55), (cx, cy + s * 1.0)], fill=RED)


def icon_building(d, cx, cy, s, color=BLUE):
    d.rectangle([cx - s * 0.45, cy - s * 0.8, cx + s * 0.45, cy + s * 0.8], fill=color)
    for r in range(3):
        for c in range(3):
            d.rectangle([cx - s * 0.32 + c * s * 0.28, cy - s * 0.6 + r * s * 0.42,
                         cx - s * 0.12 + c * s * 0.28, cy - s * 0.32 + r * s * 0.42], fill=PAPER)
    d.rectangle([cx - s * 0.18, cy + s * 0.45, cx + s * 0.18, cy + s * 0.8], fill=PAPER)
    d.line([(cx + s * 0.45, cy - s * 0.8), (cx + s * 0.45, cy - s * 1.25)], fill=color, width=4)
    d.polygon([(cx + s * 0.45, cy - s * 1.25), (cx + s * 0.95, cy - s * 1.08), (cx + s * 0.45, cy - s * 0.92)], fill=RED)


def icon_factory(d, cx, cy, s, color=BLUE):
    d.rectangle([cx - s * 0.8, cy - s * 0.1, cx + s * 0.8, cy + s * 0.7], fill=color)
    d.polygon([(cx - s * 0.8, cy - s * 0.1), (cx - s * 0.5, cy - s * 0.1), (cx - s * 0.5, cy - s * 0.5),
               (cx - s * 0.8, cy - s * 0.5)], fill=color)
    d.polygon([(cx - s * 0.2, cy - s * 0.1), (cx + s * 0.1, cy - s * 0.1), (cx + s * 0.1, cy - s * 0.5),
               (cx - s * 0.2, cy - s * 0.5)], fill=color)
    for i in range(3):
        d.rectangle([cx - s * 0.62 + i * s * 0.5, cy + s * 0.12, cx - s * 0.28 + i * s * 0.5,
                     cy + s * 0.45], fill=PAPER)


def icon_plane(d, cx, cy, s, color=BLUE):
    d.polygon([(cx - s, cy), (cx - s * 0.55, cy - s * 0.18), (cx + s * 0.35, cy - s * 0.18),
               (cx + s, cy), (cx + s * 0.35, cy + s * 0.18), (cx - s * 0.55, cy + s * 0.18)], fill=color)
    d.polygon([(cx - s * 0.1, cy - s * 0.18), (cx + s * 0.15, cy - s * 0.55), (cx + s * 0.35, cy - s * 0.18)], fill=color)
    d.polygon([(cx - s * 0.1, cy + s * 0.18), (cx + s * 0.15, cy + s * 0.55), (cx + s * 0.35, cy + s * 0.18)], fill=color)


def icon_boat(d, cx, cy, s, color=BLUE):
    d.polygon([(cx - s * 0.85, cy + s * 0.1), (cx + s * 0.85, cy + s * 0.1),
               (cx + s * 0.55, cy + s * 0.65), (cx - s * 0.55, cy + s * 0.65)], fill=color)
    d.line([(cx, cy + s * 0.1), (cx, cy - s * 0.75)], fill=color, width=4)
    d.polygon([(cx, cy - s * 0.75), (cx + s * 0.55, cy - s * 0.25), (cx, cy - s * 0.25)], fill=RED)
    for i in range(3):
        d.arc([cx - s + i * s * 0.7, cy + s * 0.7, cx - s * 0.3 + i * s * 0.7, cy + s * 1.05],
              0, 180, fill=BLUE, width=3)


def tariff_chart(d, x, y, w, h):
    """Horizontal bars: proposed US tariff rates, %."""
    data = [("INDIA", 25, RED), ("CHINA", 20, BLUE), ("EU", 15, BLUE),
            ("JAPAN", 15, BLUE)]
    label_f = SANS_B(15)
    val_f = SANS_B(17)
    row_h = h // len(data)
    max_bar = w - 130
    for i, (name, pct, col) in enumerate(data):
        ry = y + i * row_h
        d.text((x, ry + 4), name, font=label_f, fill=INK)
        bx = x + 78
        bw = int(max_bar * pct / 25)
        d.rectangle([bx, ry, bx + bw, ry + row_h - 12], fill=col)
        d.text((bx + bw + 8, ry + 4), f"{pct}%", font=val_f, fill=col)
    d.text((x, y + h + 4), "Proposed US tariff, % of goods value",
           font=SANS(13), fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 40  # margin
    # frame
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=3)
    d.rectangle([14, 14, W - 15, H - 15], outline=RULE, width=1)

    # ---- masthead ----
    y = 30
    d.text((M, y), "THE WORLD TODAY", font=SERIF_B(64), fill=INK)
    d.text((W - M - d.textlength("No. 330", font=SERIF(20)), y + 8),
           "No. 330", font=SERIF(20), fill=GREY)
    y = 108
    hline(d, M, W - M, y, 4)
    y += 10
    d.text((M, y), "THURSDAY 26 NOVEMBER 2026", font=SANS_B(26), fill=RED)
    right = "ONE DAY  •  SIX STORIES  •  THE WORLD IN A PAGE"
    d.text((W - M - d.textlength(right, font=SANS_B(15)), y + 6),
           right, font=SANS_B(15), fill=GREY)
    y += 40
    hline(d, M, W - M, y, 4)

    # ---- lead story: US tariffs on India ----
    y += 18
    lead_x, lead_w = M, W - 2 * M
    y = kicker(d, lead_x, y, "Trade  •  Washington")
    y = headline(d, lead_x, y, 620, "US PUTS 25% TARIFF ON INDIA", size=44)
    y = para(d, lead_x, y + 6, 620,
             "Washington proposes the duty after an eight-month Section 301 probe "
             "into excess manufacturing capacity. The rate falls to 17% if India "
             "signs a trade deal; New Delhi rejects the charge.",
             SANS(19), leading=25)
    # chart on the right of the lead
    tariff_chart(d, 700, 210, 244, 110)
    y = 372
    hline(d, M, W - M, y, 2)

    # ---- row 2: two stories ----
    y += 16
    row2_y = y
    col_w = (W - 2 * M - 30) // 2
    # story 2: space
    x = M
    y2 = kicker(d, x, row2_y, "Space  •  Tiangong")
    y2 = headline(d, x, y2, col_w - 90, "FIRST PAKISTANI IN ORBIT", size=30)
    y2 = para(d, x, y2 + 4, col_w - 90,
              "Muhammad Zeeshan Ali becomes the first foreign crew member aboard "
              "China's Tiangong station as Shenzhou-24 docks, alongside two "
              "Chinese crewmates.",
              SANS(18), leading=23)
    icon_rocket(d, x + col_w - 45, row2_y + 95, 42)
    # story 3: North Korea
    x = M + col_w + 30
    y3 = kicker(d, x, row2_y, "Diplomacy  •  Pyongyang")
    y3 = headline(d, x, y3, col_w - 90, "PYONGYANG EXPELS SWISS ENVOY", size=30)
    y3 = para(d, x, y3 + 4, col_w - 90,
              "North Korea orders Switzerland to close its newly opened diplomatic "
              "office and its senior diplomat to leave the country within 48 hours.",
              SANS(18), leading=23)
    icon_building(d, x + col_w - 45, row2_y + 95, 42)
    vline(d, M + col_w + 15, row2_y, row2_y + 190)
    y = row2_y + 205
    hline(d, M, W - M, y, 2)

    # ---- row 3: three stories ----
    y += 16
    row3_y = y
    col3_w = (W - 2 * M - 48) // 3
    stories = [
        ("Work  •  Dhaka", "BANGLADESH WAGE WIN",
         "Garment workers win a 36% rise in the minimum wage, a lift for "
         "millions in the world's second-biggest clothing exporter.",
         icon_factory),
        ("Security  •  Luzon", "BOMBER BUZZES PHILIPPINES",
         "A Chinese long-range bomber flies within 45 nautical miles of the "
         "Philippine coast, in a show of force Manila calls a warning.",
         icon_plane),
        ("Migration  •  Atlantic", "RECORD DAY AT CANARIES",
         "Nearly 2,000 migrants reach Spain's Canary Islands in a single day, "
         "the largest one-day arrival on record.",
         icon_boat),
    ]
    for i, (kick, head, body, icon) in enumerate(stories):
        x = M + i * (col3_w + 24)
        yy = kicker(d, x, row3_y, kick)
        yy = headline(d, x, yy, col3_w - 52, head, size=26)
        yy = para(d, x, yy + 4, col3_w, body, SANS(17), leading=22)
        icon(d, x + col3_w - 26, row3_y + 34, 26)
        if i < 2:
            vline(d, x + col3_w + 12, row3_y, row3_y + 185)
    y = row3_y + 200
    hline(d, M, W - M, y, 2)

    # ---- footer ticker ----
    y += 14
    d.text((M, y), "ALSO TODAY", font=SANS_B(18), fill=RED)
    y += 30
    ticker = ("Colombia marks 10 years since its historic peace accord  •  "
              "Australia and Solomon Islands sign a landmark security pact  •  "
              "Thanksgiving travel: long airport lines and storms across the US  •  "
              "Flipkart chief Kalyan Krishnamurthy to step down in December  •  "
              "Gukesh meets Sindarov in the World Chess Championship")
    y = para(d, M, y, W - 2 * M, ticker, SANS(17), fill=INK, leading=24)
    y += 8
    hline(d, M, W - M, y, 1, fill=(150, 145, 130))
    d.text((M, y + 8), "THE WORLD TODAY  •  All stories first reported Thursday 26 November 2026",
           font=SANS(14), fill=GREY)
    d.text((W - M - d.textlength("Page 1", font=SANS(14)), y + 8),
           "Page 1", font=SANS(14), fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} {img.size} {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
