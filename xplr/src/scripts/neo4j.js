import neo4j from "neo4j-driver"

const uri = "neo4j+s://fea84528.databases.neo4j.io"
const user = "neo4j"
const password = "DLYNNOZvZ4jb1iOQ9_IJC43x6OqQ4neClbRLIebFv8o"

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password))

export async function findOrganizationsConnectedToLocation(locationName) {
	const session = driver.session({ database: "neo4j" })

	try {
		const readQuery = `MATCH (o:Organization)-[:SERVICES]->(l:Location)
                        WHERE l.name = $locationName
                        RETURN o.name AS name`

		const readResult = await session.executeRead((tx) =>
			tx.run(readQuery, { locationName })
		)

		const organizations = readResult.records.map((record) =>
			record.get("name")
		)

		return organizations
	} catch (error) {
		console.error(`Something went wrong: ${error}`)
	} finally {
		await session.close()
	}
}
