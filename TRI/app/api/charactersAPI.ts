const DB = 'http://localhost:4000'

export async function getChars() {
    const res = await fetch(`${DB}/characters`)
    if (!res.ok) throw new Error()
    return res.json()
}

export async function getCharById(id: string) {
    if (!id) throw new Error('ID персонажа обязателен')

    const res = await fetch(`${DB}/characters/${id}`)
    if (!res.ok) {
        if (res.status === 404) {
            throw new Error('Персонаж не найден')
        }
        throw new Error('Ошибка при загрузке персонажа')
    }
    return res.json()
}

export async function postChar(char: Object) {
    const res = await fetch(`${DB}/characters`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(char)
    })

    if (!res.ok) throw new Error()
    return res.json()
}

export async function patchChar(
    char: {id: string, [key: string]: any}) {
    const res = await fetch(`${DB}/characters/${char.id}`, {
        method: 'PATCH',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(char)
    })

    if (!res.ok) throw new Error()

    return res.json()
}

export async function deleteChar(id: string) {
    const res = await fetch(`${DB}/characters/${id}`, {
        method: 'DELETE'
    })

    if (!res.ok) throw new Error()
}