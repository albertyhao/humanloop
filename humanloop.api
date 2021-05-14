const child_process = require('child_process');
const path = require('path');
const fs = require('fs');

let saver;
function initialize() {
	saver = require('../saver/app.js');
}
function addRoutes(app) {

	//POST request to server to run command
	app.post('/humanloop/python', (req, res, next) => {

		//const filepath = path.join(__dirname, '../../libs/python/code.py' )

		//makes a random python file
		const filepath = '/tmp/'+Math.random()+'.py';
		fs.writeFileSync(filepath, req.body.code, 'utf8');

		//forks and exec() a pylint command line operation
		child_process.exec(`pylint ${filepath}`, (err, sysout, syserr) => {
			res.send(`<pre>${sysout.toString('utf8')}</pre>`); //sends pylint output message
		})
	})

	//GET request to run snork.py and return
	app.get('/humanloop/run', (req, res, next) => {
		// access Qoom database
		saver.getFile().then(model => {
			//use RegEx to iterate through /rules dir
			model.find({isBackup: false, domain: req.headers.host, name: /^humanloop\/rules\/.*\.py$/}).lean().exec((err, docs) => {
				//find snork.py
				const snork = docs.find(d => d.name.endsWith('snork.py'))
				//filter files that are not snork or utils to get rules function files
					, files = docs.filter(d => !d.name.endsWith('snork.py') && !d.name.endsWith('utils.py'))
					//define imports to contents of rules files
					, imports = files.map(f => {
						//format rules functions
						const method = f.contents
							.trim()
							.split('\n')
							.find(l => l.trim().startsWith('def'))
							.replace('def', '')
							.split('(')[0]
						if(!method) return '';
						// put import statement into imports object
						return `from ${path.parse(f.name).name.replace(/\.py$/, '')} import ${method.trim()}`
					})
					// replace imports substitute with import statements
					, snorkcode = snork.contents.replace('{{IMPORTS}}', imports)
				;

				const filename = 'humanloop/rules/snorkwithimports.py';
				const filepath = path.join(__dirname, '../../libs/', filename);
				const spamfolder = path.parse(filepath).dir;
				fs.writeFileSync(filepath, snorkcode, 'utf8');
			//	return res.send(snorkcode)

				// exec python operation for snork.py with imported rules functions
				child_process.exec(`python ${filepath}`, {
					cwd: spamfolder
				}
				//send the output, errors, command errors (formatted)
				, (err, sysout, syserr) => {
					res.send(`
						Output
						<pre>${sysout.toString('utf8')}</pre>
						Error
						<pre>\n${syserr.toString('utf8')}</pre>
						Command Error
						<pre>${err}</pre>`);
				})
			})
		})
		//const spamfilepath = path.join(spamfolder, (Math.random() + '' + new Date()*1).replace('.', '')+'.py');
		//fs.writeFileSync(spamfilepath, code, 'utf8');

		// //return res.send(spamfolder)
	})
}

module.exports = {
	initialize, addRoutes
}
