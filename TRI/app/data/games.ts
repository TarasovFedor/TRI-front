import type { Genre } from './genres';

export interface Game{
    gameId:number,
    gameName:string,
    gameAuthorId:number,
    gameGenres: Genre[],
    gameFollowers:number,
    gameIcon:string,
    gameStatus:string,
    gameDescription:string,
}

export const GAMES: Game[] = [
    {
        gameId:0,
        gameName:'Название игры 1',
        gameAuthorId:123,
        gameGenres:[{id:0,name:'жанр1'},{id:0,name:'жанр2'}],
        gameFollowers:12,
        gameIcon:'https://i.pinimg.com/736x/04/91/fc/0491fc12a230f0013e3e563be70ac725.jpg',
        gameStatus:'Октрыто',
        gameDescription:'Это описания игры 1',
    },
    {
        gameId:1,
        gameName:'Название игры 2',
        gameAuthorId:34,
        gameGenres:[{id:4,name:'жанр5'},{id:5,name:'жанр6'}],
        gameFollowers:12,
        gameIcon:'https://i.pinimg.com/736x/04/91/fc/0491fc12a230f0013e3e563be70ac725.jpg',
        gameStatus:'Закрыто',
        gameDescription:'Это описания игры 2'
    }
]