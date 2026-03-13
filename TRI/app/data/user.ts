import type {Genre} from "./genres"
import type { Game } from "./games"
import type { Character } from "./characters"
import { GAME_GENRES } from "./genres"
import { GAMES } from "./games"
import { CharExample } from "./characters"

export interface User {
    userId: number,
    userIcon: string
    userName: string,
    userEmail: string,
    userType: string,
    userDesc: string,
    userFavGenres: Genre[],
    userUnfavGenres: Genre[],
    userFavGames: Game[],
    userCharList: Array<Character>
}

export const UserExample: User = {
    userId: 0,
    userName: 'Example',
    userIcon: 'https://i.pinimg.com/736x/04/91/fc/0491fc12a230f0013e3e563be70ac725.jpg',
    userEmail: 'example@mail.com',
    userType: 'manual',
    userDesc: 'example',
    userFavGenres: GAME_GENRES,
    userUnfavGenres: GAME_GENRES,
    userFavGames: GAMES,
    userCharList: [CharExample, CharExample, CharExample]
}