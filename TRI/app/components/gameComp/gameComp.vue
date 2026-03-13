<template>

<div class="game">
    <div class="game-header">
        <img :src="props.game.gameIcon">
        <div class="game-name">
            <h3>Название игры: {{ props.game.gameName }}</h3>
            <p>#{{ props.game.gameAuthorId }}</p>
            <p>Статус игры: {{ props.game.gameStatus }}</p>
        </div>
    </div>
    <h3 class="game-description">
        Описание игры:
        <p>
            {{ props.game.gameDescription }}
        </p>
    </h3>
    <div class="genres">
        <span v-for="(genre,index) in props.game.gameGenres">
            {{ genre.name }}
        </span>
    </div>
    <div class="line"></div>
    <p>Участников: {{ props.game.gameFollowers }}</p>
</div>

</template>

<script setup lang="ts">
import type { Game } from '~/data/games';
const props = defineProps<{
    game: Game,
}>()

</script>

<style scoped>
.game{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    border-bottom: 1px black solid;
    padding: 5px;
    margin-bottom: 10px;
}
.game-header{
    display: flex;
    gap: 10px 20px;
}
.game-header img{
    width: 10%;
    object-fit: cover;
    border-radius: 100px;
}
.genres{
    display: flex;
    gap: 5px;
}
.genres span{
    font-size: 10px;
    background-color: rgb(213, 213, 213);
    padding: 2px 3px;
    border-radius: 2px;
}
</style>