import React, { useEffect, useRef } from "react"
import * as d3 from "d3"
import * as d3Force from "d3-force"

export default function GraphVisualization({ nodes, relationships }) {
	const svgRef = useRef(null)

	useEffect(() => {
		// if (!nodes || !relationships) return // add null check
		if (svgRef.current) {
			const svg = d3.select(svgRef.current)

			// Set up the simulation
			const simulation = d3Force
				.forceSimulation(nodes)
				.force(
					"link",
					d3Force
						.forceLink(relationships)
						.id((d) => d.id)
						.distance(100)
				)
				.force("charge", d3Force.forceManyBody().strength(-500))
				.force("center", d3Force.forceCenter())

			// Add nodes and links to the visualization
			const link = svg
				.append("g")
				.selectAll("line")
				.data(relationships)
				.enter()
				.append("line")
				.attr("stroke", "black")
			const node = svg
				.append("g")
				.selectAll("circle")
				.data(nodes)
				.enter()
				.append("circle")
				.attr("r", 20)
				.attr("fill", "blue")

			// Add forces to the simulation
			simulation.on("tick", () => {
				link.attr("x1", (d) => d.source.x)
					.attr("y1", (d) => d.source.y)
					.attr("x2", (d) => d.target.x)
					.attr("y2", (d) => d.target.y)
				node.attr("cx", (d) => d.x).attr("cy", (d) => d.y)
			})
		}
	}, [nodes, relationships])

	return <svg ref={svgRef} />
}
