import React, { useState, useEffect } from "react"
import { OrgNode, Relationship, LocationNode, LifecycleNode } from "../models"

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
		var locationConns
		var lifecycleConns
		organizations.forEach((org, index) => {
			locationConns = org.location.map(
				(loc, idx) =>
					new Relationship(index, org, null, "SERVICES", null)
			)
			lifecycleConns = org.lifecycles.map(
				(lf, idx) =>
					new Relationship(index, org, null, "SERVICES", null)
			)
		})

		setRelationhips(locationConns.concat(lifecycleConns))
	}

	useEffect(() => {
		buildNodes()
		buildRelatonships()
	}, [organizations, nodes, relationhips])

	return <div>Graph</div>
}
