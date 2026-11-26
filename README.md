# The World Today — Thursday 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/yuyan5319-crypto/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/yuyan5319-crypto/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

One image that sums up the world's news of **Thursday 26 November 2026**,
drawn as a newspaper front page: [make.fun bounty](https://make.fun/bounty/news-image-20261126).

## The stories

1. **US puts 25% tariff on India** — Washington proposes the duty after a Section 301 probe; 17% if a trade deal is signed.
2. **First Pakistani in orbit** — Muhammad Zeeshan Ali becomes the first foreign crew member aboard China's Tiangong station as Shenzhou-24 docks.
3. **Pyongyang expels Swiss envoy** — North Korea orders Switzerland to close its new Pyongyang office within 48 hours.
4. **Bangladesh wage win** — Garment workers win a 36% rise in the minimum wage.
5. **Bomber buzzes Philippines** — A Chinese long-range bomber flies within 45 nautical miles of the Philippine coast.
6. **Record day at Canaries** — Nearly 2,000 migrants reach Spain's Canary Islands in a single day.

Footer ticker: Colombia marks 10 years since its peace accord; Australia and
Solomon Islands sign a security pact; US Thanksgiving travel hit by long lines
and storms; Flipkart chief to step down; Gukesh meets Sindarov in the World
Chess Championship.

## How to run it

`draw.py` (Python + Pillow, build time only) draws `entry.png` (1024x1024).
`main.py` (stdlib only, no network) copies it to the output directory:

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` runs in the grading sandbox (Python 3.13, stdlib only) and writes
the same bytes on every run.

## License

MIT — see [LICENSE](LICENSE).
