<template>
    <section class="profile">
        <div class="cont profile__cont">
            <img class="avatar" :src = "UserExample.userIcon" alt="">

            <div class="user-info">
                <h2 class="profile__name">Имя пользователя</h2>
                <div class="profile__rang">
                    <div class="rang-img" src="" alt=""></div>
                    <p class="profile__text">Ранг</p>
                </div>
                <ul class="networks__list">
                        <li class="networks__item">
                            <a href="" class="networks__link">
                                <img src="../icon/footer-networks/vk.svg" alt="" class="networks__icon">
                            </a>
                        </li>
                        <li class="networks__item">
                            <a href="" class="networks__link">
                                <img src="../icon/footer-networks/Telegram.svg" alt="" class="networks__icon">
                            </a>
                        </li>
                        <li class="networks__item">
                            <a href="" class="networks__link">
                                <img src="../icon/footer-networks/mail.svg" alt="" class="networks__icon">
                            </a>
                        </li>
                    </ul>
                <label class="profile__text" for="desc">О пользователе</label>
                <textarea class="profile__textarea" name="" id="desc"></textarea>
                <div class="select-cont">
                    <label for="type-profile">Тип профиля</label>
                    <select class="select" name="profile" id="type-profile">
                            <option value="open">открытый</option>
                            <option value="open">открытый только для друзей</option>
                            <option value="close">закрытый</option>
                    </select>
                </div>
                
            </div>
                <!-- <p>Любимые жанры</p>
                <ul class="genresList">
                    <li class="genre" v-for = "Genre in UserExample.userFavGenres">
                        {{Genre.name}}
                    </li>
                </ul>

                <p>Избранные квесты/игры</p>
                <ul class="gamesList">
                    <li class="game" v-for = "Game in UserExample.userFavGames">
                        {{Game.gameName}}
                    </li>
                </ul> -->

                <!-- <p>Персонажи</p>
                <ul class="charList">
                    <li v-for = "Char in UserExample.userCharList">
                        <img class="charImg" :src = "Char">
                    </li>
                </ul> -->            
        </div>
    </section>
</template>

<script setup lang="ts">
    import {UserExample} from '~/data/user'
    definePageMeta({
    layout: 'main'
    })

    const query = useRoute().params.id
</script>

<style scoped>
    .profile{
        background-color: #F4F4F5;
    }
    .profile__cont{
        display: flex;
        align-items: start;
        gap: 2rem;
        padding-top: 6.5rem;
        justify-content: center;
    }
    .avatar {
        margin-top: 16px;
        border-radius: 50%;
        border: 1px solid #D9D9D9;
        width: 15rem;
        aspect-ratio: 1;
    }

    .genresList {
        display: flex;
        gap: 30px
    }

    .genre {
        background-color: grey;
        padding: 3px 7px
    }

    .gamesList {
        display: flex;
        flex-direction: column;
        gap: 16px
    }

    .game {
        width: fit-content;
        background-color: grey;
        padding: 3px 7px
    }
    .user-info{
        max-width: 50rem;
        margin-bottom: 20rem;
    }
    .charList {
        display: flex;
        align-items: flex-start;
        gap: 30px;
    }

    .charImg {
        border-radius: 50%;
        object-fit: cover;
        border: solid black;
        width: 150px;
        aspect-ratio: 1;
    }

    .profile__name{
        font-size: 4rem;
        color: var(--color-blue);
        font-weight: 400;

    }
    .rang-img{
        width: 4rem;
        height: 4rem;
        background-color: #C2A27733;
        border-radius: 50%;

    }
    .profile__rang{
        display: flex;
        gap: 1rem;
        align-items: center;
        margin-bottom: 1rem;
    }

    .profile__text, label{
        font-size: 1.6rem;
        color: var(--color-blue)
    }
    .networks{
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }
    .networks__list{
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 1rem;
        margin-bottom: 4rem;
    }
    .profile__textarea{
        width: 50rem;
        height: 10rem;
        border: 1px solid #D9D9D9;
        border-radius: 1rem;
        margin-bottom: 3rem;
    }
    .select-cont{
        display: flex;
        gap: 10rem
    }
    .select{
        color: var(--color-blue);
        border: 1px solid #D9D9D9;
        width: 30rem;
        height: 3rem;
        border-radius: .5rem;
        font-size: 1.4rem;
        padding-inline: 1rem;
    }

</style>