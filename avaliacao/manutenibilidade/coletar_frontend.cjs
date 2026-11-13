const fs = require('fs');
const path = require('path');
const { ESLint } = require('eslint');
const madge = require('madge');
(async () => {
  const [root, out, inventory] = process.argv.slice(2);
  const web = path.join(root, 'web');
  const files = JSON.parse(fs.readFileSync(inventory)).incluidos.filter(f=>f.startsWith('web/'));
  const ts = JSON.parse(fs.readFileSync(path.join(web,'tsconfig.json')));
  ts.compilerOptions.baseUrl = web;
  const graph = await madge(files.map(f=>path.join(root,f)), {baseDir:web,fileExtensions:['ts','tsx'],tsConfig:ts,detectiveOptions:{ts:{skipTypeImports:false},tsx:{skipTypeImports:false}}});
  fs.writeFileSync(path.join(out,'madge.json'),JSON.stringify(graph.obj(),null,2));
  fs.writeFileSync(path.join(out,'madge-warnings.json'),JSON.stringify(graph.warnings(),null,2));
  for (const limit of [0,10]) {
    const eslint = new ESLint({cwd:web,useEslintrc:false,ignore:false,baseConfig:{parser:require.resolve('@typescript-eslint/parser'),parserOptions:{ecmaVersion:2022,sourceType:'module',ecmaFeatures:{jsx:true}},rules:{complexity:['error',limit]}}});
    const results = await eslint.lintFiles(files.map(f=>path.join(root,f)));
    fs.writeFileSync(path.join(out,`eslint-${limit}.json`),JSON.stringify(results,null,2));
  }
})().catch(e=>{console.error(e);process.exit(1)});
