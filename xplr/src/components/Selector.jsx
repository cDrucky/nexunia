import React, { useState, useEffect } from "react"

const cities = ["Harrisburg", "York", "Lancaster"]
const lifecycles = ["Idea", "Seed", "Startup", "Growth", "Mature", "Exit"]

export default function Selector({ updateForm }) {
	const [city, setCity] = useState("Harrisburg")
	const [lifecycle, setLifecycle] = useState("Idea")
	const handleCityChange = (event) => {
		setCity(event.target.value)
	}

	const handleLifecycleChange = (event) => {
		setLifecycle(event.target.value)
	}

	const buildDropdown = (items, label, fr, state, change) => {
		const ops = items.map((item) => <option value={item}>{item}</option>)
		return (
			<div>
				<label htmlFor={fr}>{label}</label>
				<select id={fr} value={state} onChange={change}>
					{ops}
				</select>
			</div>
		)
	}

	useEffect(() => {
		updateForm({ city, lifecycle })
	}, [city, lifecycle, updateForm])

	return (
		<>
			{buildDropdown(
				cities,
				"Select a city: ",
				"city-select",
				city,
				handleCityChange
			)}
			{buildDropdown(
				lifecycles,
				"Select a lifecycle: ",
				"lifecycle-select",
				lifecycle,
				handleLifecycleChange
			)}
		</>
	)
}
