<template>

    <div class="search-block">
        <div class="input-block">
            <input type="text" placeholder="Название игры">
            <button>Найти</button>
        </div>
        <div class="gnrs">
                <span class="genre" v-for="(genre,index) in GAME_GENRES">
                    {{ genre.name }}
                </span>
            </div>
        <button class="create-game-btn">Создать игру</button>
    </div>

</template>


<script setup>
import {GAME_GENRES}  from '../../data/genres'



</script>



<style scoped>
.gnrs{
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    gap: 5px 5px;
    padding: 4px 0px;
}

.genre{
    padding:3px 5px;
    background-color: rgb(186, 186, 186);
    cursor: pointer;
    border-radius: 7px;
}

.search-block{
    width: 70%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.input-block{
    display: flex;
    width: 100%;
    justify-content: space-between;
    padding: 5px;
}

.input-block input{
    width: 75%;
    padding: 5px 1px;
    outline: none;
}
.input-block button{
    background-color: white;
    border-width: 0px;
    width: 125px;
    border: 1px black solid;
    border-radius: 7px;
    cursor: pointer;
}

.create-game-btn{
    width: 90%;
    padding: 10px;
    background-color: white;
    margin: 10px 0px;
    font-size: 16px;
    border-width: 0px;
    border-radius: 7px;
    background-color: #0051A8;
    color: white;
}


</style>