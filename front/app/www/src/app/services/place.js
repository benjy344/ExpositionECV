export function getPlaceData(id=1) {

    return fetch(`http://pitipoulpe.freeboxos.fr/api/places/${id}`)
}