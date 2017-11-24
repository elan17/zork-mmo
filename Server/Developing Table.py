from Server.Objects.Sala import Sala
from Server.Objects.Subclases.Door import Door
from Server.Objects.Subclases.Container import Container
from Server.World_Handler import create_sala_entry
from Server.Config import Archivo
from Server.Object_pickler import generate_key

config = Archivo("./config.conf")  # Cargamos la configuración del servidor
generate_key(config)

import Server.Login  # Generamos la base de datos de usuarios si no existe

Spawn = Sala("SPAWN", (0, 0, 0), {"NORTH": (1, 0, 0)})

prueba = Sala("PRUEBA", (1, 0, 0), {"SOUTH": (0, 0, 0)})

contenedor = Container("COCOPEYE", "jorl")

puerta = Door("gold_door", "DOOR", coords=((0, 0, 0), (1, 0, 0)))
puerta.set_atribute("description", "gold_door_description")

Spawn.set_atribute("description", "spawn_room_description")

Spawn.add_entity_def(puerta)
Spawn.add_entity_def(contenedor)
prueba.add_entity_def(puerta)

create_sala_entry(Spawn, config)
create_sala_entry(prueba, config)
