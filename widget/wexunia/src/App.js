import React, { useState, useEffect } from "react"
import neo4j from "neo4j-driver"

const db_user = process.env.REACT_APP_DATABASE_USER
const db_pass = process.env.REACT_APP_DATABASE_PASSWORD
const db_host = process.env.REACT_APP_DATABASE_HOST

const driver = neo4j.driver(db_host, neo4j.auth.basic(db_user, db_pass))

function App() {
	const [nodes, setNodes] = useState([])

	useEffect(() => {
		const session = driver.session()

		session
			.run("MATCH (n) RETURN n LIMIT 10")
			.then((result) => {
				const nodes = result.records.map((record) => record.get("n"))
				setNodes(nodes)
			})
			.catch((error) => console.error(error))
			.finally(() => session.close())
	}, [])

	return (
		<div>
			TESTING
			<h1>Neo4j Nodes:</h1>
			<ul>
				{nodes.map((node) => (
					<li key={node.identity.toString()}>
						{JSON.stringify(node.properties)}
					</li>
				))}
			</ul>
		</div>
	)
}

export default App
