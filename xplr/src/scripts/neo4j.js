import neo4j from "neo4j-driver"

const uri = process.env.REACT_APP_NEO4J_URI
const user = process.env.REACT_APP_NEO4J_USER
// const password = "DLYNNOZvZ4jb1iOQ9_IJC43x6OqQ4neClbRLIebFv8o"
const password = process.env.REACT_APP_NEO4J_PASSWORD
const driver = neo4j.driver(uri, neo4j.auth.basic(user, password))

export async function findOrganizationsConnectedToLocation(
	locationName,
	lifecycleName
) {
	const session = driver.session({ database: "neo4j" })

	try {
		const readQuery = `
			MATCH (o:Organization)-[:SERVICES]->(l:Location)
			WHERE l.name = "${locationName}"
			MATCH (o)-[:PROVIDES]->(s:Lifecycle)
			WHERE s.name = "${lifecycleName}"
			RETURN 
				o.name AS name, 
				o.address AS address, 
				o.location AS location, 
				o.notes AS notes, 
				o.website AS website,
				COLLECT(DISTINCT l.name) AS locations,
				COLLECT(DISTINCT s.name) AS lifecycles`

		const readResult = await session.executeRead((tx) => tx.run(readQuery))

		const organizations = readResult.records.map((record) => ({
			name: record.get("name"),
			address: record.get("address"),
			location: record.get("location"),
			notes: record.get("notes"),
			website: record.get("website"),
			locations: record.get("locations"),
			lifecycles: record.get("lifecycles"),
		}))

		return organizations
	} catch (error) {
		console.error(`Something went wrong: ${error}`)
	} finally {
		await session.close()
	}
}
