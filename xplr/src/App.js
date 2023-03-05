import React, { useState, useEffect } from "react"
import { findOrganizationsConnectedToLocation } from "./scripts/neo4j"
import { Selector, Graph } from "./components"

function App() {
	const [organizations, setOrganizations] = useState([])
	const [form, setForm] = useState({ city: "Harrisburg", lifecycle: "Idea" })

	useEffect(() => {
		async function fetchData() {
			const data = await findOrganizationsConnectedToLocation(
				form.city,
				form.lifecycle
			)
			setOrganizations(data)
		}
		fetchData()
	}, [form.city, form.lifecycle]) // update the organizations when city changes

	return (
		<div>
			<h1>Organizations Connected to {form.city}</h1>
			<Selector updateForm={setForm} />
			<ul>
				{organizations.map((org, index) => (
					<li key={index}>
						{org.name} - {org.website}
					</li>
				))}
			</ul>
			<Graph organizations={organizations} />
		</div>
	)
}

export default App
