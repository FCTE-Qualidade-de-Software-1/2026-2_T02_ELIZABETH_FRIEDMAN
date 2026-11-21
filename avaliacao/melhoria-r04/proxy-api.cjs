// Proxy local somente leitura para a API pública do Sua Grade UnB.
// Repassa apenas GET (disciplinas e períodos). Login e gravações não saem da máquina:
// POST /users/login/ responde 401 (o site fica no modo anônimo) e os demais POST/DELETE respondem 403.
const http = require('node:http');
const https = require('node:https');

const PORT = 8999;
const API = 'api.suagradeunb.com.br';

http.createServer((req, res) => {
  const origin = req.headers.origin || '*';
  const cors = {
    'access-control-allow-origin': origin,
    'access-control-allow-credentials': 'true',
    'access-control-allow-headers': 'content-type, authorization, accept',
    'access-control-allow-methods': 'GET, POST, DELETE, OPTIONS',
  };
  if (req.method === 'OPTIONS') { res.writeHead(204, cors); return res.end(); }
  if (req.method !== 'GET') {
    const status = req.url.startsWith('/users/login/') ? 401 : 403;
    console.log(`${req.method} ${req.url} -> ${status} (bloqueado)`);
    res.writeHead(status, { ...cors, 'content-type': 'application/json' });
    return res.end('{}');
  }
  const up = https.request({ host: API, path: req.url, method: 'GET', headers: { accept: 'application/json' } }, r => {
    console.log(`GET ${req.url} -> ${r.statusCode}`);
    res.writeHead(r.statusCode, { ...cors, 'content-type': r.headers['content-type'] || 'application/json' });
    r.pipe(res);
  });
  up.on('error', e => { res.writeHead(502, cors); res.end(JSON.stringify({ erro: e.message })); });
  up.end();
}).listen(PORT, '127.0.0.1', () => console.log(`Proxy em http://127.0.0.1:${PORT}`));
