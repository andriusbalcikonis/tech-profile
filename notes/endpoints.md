# App special endpoints

Version endpoint:

- Will be useful for this application after deploy checks
- Could be useful for other apps pre-deploy dependency checks

Liveness & readyness endpoints:

- When app is just starting up and we need just to wait – it’s alive, but not yet ready. No restart it needed or anything.
- When app is having problems, it should be not alive.
- Used by `kubernetes` liveness & readyness probes
