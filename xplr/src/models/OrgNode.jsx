export default class OrgNode {
	constructor(id, label, website, address, location) {
		this.id = id
		this.label = label
		this.website = website
		this.address = address
		this.location = location
		this.x = 0 // default x-position
		this.y = 0 // default y-position
		this.radius = 10 // default radius
		this.color = "#ccc" // default color
	}
}
