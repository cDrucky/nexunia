import React, { useState, useEffect } from "react"
import { findOrganizationsConnectedToLocation } from "./scripts/neo4j"

function App() {
	const [organizations, setOrganizations] = useState([])

	useEffect(() => {
		async function fetchData() {
			const data = await findOrganizationsConnectedToLocation(
				"Harrisburg"
			)
			setOrganizations(data)
		}
		fetchData()
	}, [])

	return (
		<div>
			<h1>Organizations Connected to Harrisburg</h1>
			<ul>
				{organizations.map((org, index) => (
					<li key={index}>{org}</li>
				))}
			</ul>
		</div>
	)
}

export default App
