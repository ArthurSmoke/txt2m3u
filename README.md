# txt2m3u

## 简介

通过 Github Action 定制更新，转换指定 IPTV TXT 链接为 M3U 格式文件

## 使用方法

folk 本项目
设置相应的 secret

| secret     | note                                      |
| ---------- | ----------------------------------------- |
| FILE_PATH  | 需要装换的在线 txt url                    |
| TG_TOKEN   | 发送 push 的 telegram bot token           |
| TG_TALK_ID | 发送 push 的 telegram bot talk ID         |
| DATA       | 存放 m3u 文件的仓库全名                   |
| TOKEN      | github token,用于更新仓库，需要 repo 权限 |
