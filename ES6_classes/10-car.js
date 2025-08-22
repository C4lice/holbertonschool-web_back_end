export default class Car{
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    var hasSpecies = this.constructor[Symbol.species];
    var cloneObject = hasSpecies? new this.constructor[Symbol.species]() : new this.constructor();
    cloneObject._brand = this._brand;
    cloneObject._motor = this._motor;
    cloneObject._color = this._color;
    return cloneObject;
  }
}
