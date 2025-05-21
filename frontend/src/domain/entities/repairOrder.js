export class RepairOrder {
    constructor({ id, id_vehiculo, fecha_inicio, fecha_fin, estado, mano_de_obra, prioridad, details }) {
      this.id = id;
      this.id_vehiculo = id_vehiculo;
      this.fecha_inicio = fecha_inicio;
      this.fecha_fin = fecha_fin;
      this.estado = estado;
      this.mano_de_obra = mano_de_obra;
      this.prioridad = prioridad;
      this.details = details || [];
    }
  }