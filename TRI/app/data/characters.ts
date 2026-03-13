import type { User } from "./user";
import type { Game } from "./games";
import { GAMES } from "./games";
import { UserExample } from "./user";

export interface Character {
    id?: number,
    name: string,
    icon: string,
    stats: Object,
    description: string,
    authorId: number,
    gameId: number
}

export const CharExample: Character = {
    id: 0,
    name: 'Harry Maguire',
    icon: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo1y6D0SXycGzllo7u_Nds-Ig51YzVmKRorQ&s',
    stats: {
        overall: 80,
        position: 'CB',
        country: 'England',
        pace: 35,
        shots: 57,
        passing: 70,
        dribbling: 65,
        defending: 80,
        physical: 82
    },
    description: 'Харри Магуайр – английский футболист, центральный защитник, известный своей физической мощью, силовой игрой и лидерскими качествами.',
    authorId: 0,
    gameId: 0
}