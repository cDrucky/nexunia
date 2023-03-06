export default class Relationship {
	constructor(id, source, target, type, properties) {
		this.id = id
		this.source = source
		this.target = target
		this.type = type
		this.properties = properties
	}
}
