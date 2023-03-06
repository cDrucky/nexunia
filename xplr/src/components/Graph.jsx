import React, { useState, useEffect } from "react"
import { OrgNode, Relationship, LocationNode, LifecycleNode } from "../models"
import { GraphVisualization } from "."

const locations = ["Harrisburg", "York", "Lancaster"]
const lifecycles = ["Idea", "Seed", "Startup", "Growth", "Mature", "Exit"]

export default function Graph({ organizations }) {
	const [nodes, setNodes] = useState([])
	const [relationhips, setRelationhips] = useState([])

	const buildNodes = () => {
		const locationNodes = locations.map(
			(loc, idx) => new LocationNode(idx, loc)
		)
		const lifecycleNodes = lifecycles.map(
			(lf, idx) => new LifecycleNode(idx, lf)
		)
		const orgsNodes = organizations.map(
			(org, idx) =>
				new OrgNode(
					idx,
					org.name,
					org.website,
					org.address,
					org.location
				)
		)
		const allNodes = orgsNodes.concat(locationNodes, lifecycleNodes)

		setNodes(allNodes)
	}

	const buildRelatonships = () => {
		const relationships = []

		organizations.forEach((org, index) => {
			const locationConns = org.locations.map((loc, idx) => {
				return new Relationship(index, org, null, "SERVICES", null)
			})

			const lifecycleConns = org.lifecycles.map((lf, idx) => {
				return new Relationship(index, org, null, "SERVICES", null)
			})

			relationships.push(...locationConns, ...lifecycleConns)
		})
		setRelationhips(relationhips)
	}

	useEffect(() => {
		buildNodes()
		buildRelatonships()
	}, [organizations, nodes, relationhips])

	return (
		<GraphVisualization
			nodes={nodes ? nodes : []}
			relationhips={relationhips ? relationhips : []}
		/>
	)
}
