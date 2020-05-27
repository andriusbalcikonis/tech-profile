# Next.js static site generator

Dependencies: `docker` and `docker-compose`

To run:

1. `docker-compose up`
2. Open http://localhost:8061

To export static files for CDN hosting:

1. `docker-compose run nextjs npm run export`
2. Take `./nextjs/out` dir

This example demonstrates the framework itself and is extremely minimalistic. For example of nice free design template, see `example-of-free-template`.
