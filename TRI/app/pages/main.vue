<template>
    <section class="main_blue">
        <div class="cont main__content">
            <h1 class="main__title">Приглашаем на платформу создания текстовых ролевых игр </h1>
            <p class="main__text">ТПИ - Идеальная среда для ваших историй.</p>
            <button class="btn btn_white">Начать игру</button>
            <div class="main__image"></div>
        </div>
    </section>

    <section class="characters">
        <div class="cont">
            <span class="line"></span>
            <h2 class="characters__title">
                Для кого наша платформа
            </h2>
            <div class="cards">
                <div class="card">
                    <h3 class="card__title">Гейм-мастера</h3>
                    <p class="card__description">Создавай игры, используя широкий функционал платформы. Находи активных игроков и получай удовольствие.</p>
                </div>
                <div class="card card_second">
                    <h3 class="card__title">Игроки</h3>
                    <p class="card__description">Думаешь, что тебе сложно угодить? Уверены, мы найдем чем тебя удивить. У нас большой выбор активных игр и удобный поиск.</p>
                </div>
                <div class="card">
                    <h3 class="card__title">Писатели</h3>
                    <p class="card__description">Три платформа — твой шанс заявить о себе и получить признание в ролевом сообществе. Публикуй свои работы и забирайся на вершину популярности.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="advantages">
        <div class="cont">
            <h2 class="advantages__title">
                Почему мы?
            </h2>
            <div class="advantages__cards">
                <div class="card-advantage">
                    <img src="../icon/advantage/Friends.svg" alt="">
                    <h3 class="card-advantage__title">Найдите своих людей</h3>
                    <p class="card-advantage__desc">
                        Знакомьтесь с игроками, которые разделяют ваши увлечения, и добавляйте их в друзья! Общайтесь в личных сообщениях, делитесь впечатлениями, шутками и, конечно же, свежими мемами.
                    </p>
                </div>
                <div class="card-advantage">
                    <img src="../icon/advantage/Free.svg" alt="">
                    <h3 class="card-advantage__title">Никаких барьеров. Никакой платы.</h3>
                    <p class="card-advantage__desc">
                        Просто заведите аккаунт — и играйте в своё удовольствие.
                    </p>
                </div>
                <div class="card-advantage">
                    <img src="../icon/advantage/gamepad.svg" alt="">
                    <h3 class="card-advantage__title">Игры</h3>
                    <p class="card-advantage__desc">
                        Многофункциональные игровые платформы предоставят вам всё необходимое: от интерактивных карт и виртуальных костей до площадок для обсуждений и новостных лент, где оживает ваш мир.
                    </p>
                </div>
                <div class="card-advantage">
                    <img src="../icon/advantage/world.svg" alt="">
                    <h3 class="card-advantage__title">Играйте где угодно</h3>
                    <p class="card-advantage__desc">
                        Ваш мир — в вашем кармане. Запускайте игру в браузере любого устройства: будь то мощный компьютер или смартфон в дороге. Никаких границ!
                    </p>
                </div>
                <div class="card-advantage">
                    <img src="../icon/advantage/Notification.svg" alt="">
                    <h3 class="card-advantage__title">Объявления</h3>
                    <p class="card-advantage__desc">
                        Игра найдётся для всех!Не можете найти подходящую игру или игроков? Создайте объявление с вашими предпочтениями — и отклики не заставят себя ждать. 
                    </p>
                </div>
            </div>
            <div class="center">
                <button class="btn">Начать игру</button>
            </div>
        </div>
    </section>
</template>

<script setup>
definePageMeta({
  layout: 'first-page'
})

</script>

<style scoped>

.main_blue{
    background-color:#0051A8;
    padding: 3rem;
    max-height: 75rem;
    margin-bottom: 36rem;
}
.main__content{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.main__title{
    font-size: 4.8rem;
    font-weight: 400;
    text-align: center;
    color: #fff;
    margin-bottom: 4.6rem;
    width: 80%;
}
.main__text{
    text-align: center;
    color: #fff;
    font-size: 3.2rem;
    margin-bottom: 2.5rem;
}
.btn_white{
    background-color: #fff;
    color: #0051A8;
    display: inline-block;
    margin-bottom: 3rem;
}
.main__image{
    background-color: grey;
    height: 60rem;
    width: 70%;
}
.characters{
    margin-bottom: 20rem;
}
.line{
    display: block;
    height: 1px;
    background-color: #878794;
}

.characters__title{
    font-size: 6.4rem;
    font-weight: 400;
    margin-bottom: 4rem;
}
.cards{
    display: flex;
    flex-direction: row;
    gap: 5.6rem;
}
.card{
    background-color: var(--color-blue);
    width: 40rem;
    height: 30rem;
    border-radius: 1rem;
    padding: 2rem;
    opacity: 30%;
}
.card_second{
    margin-block: 16rem;
}
.card__title{
    font-size: 3.6rem;
    color: var(--color-light);
    text-align: center;
    margin-bottom: 1.2rem;
}
.card__description{
    font-size: 2rem;
    text-align: center;
}

.advantages{
    margin-bottom: 10rem;
}
.advantages__title{
    text-align: center;
    color: var(--color-blue);
    font-size: 6.4rem;
    font-weight: 400;
    margin-bottom: 5rem;
}
.advantages__cards{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
    margin-bottom: 7.5rem;
}
.card-advantage{
    width: 32rem;
    border: 1px solid #878794;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    gap: 2rem;
    border-radius: 1rem;
}
.card-advantage__title{
    text-align: center;
    color: var(--color-blue);
    font-size: 1.8rem;
}
.card-advantage__desc{
    text-align: center;
    font-size: 1.6rem;
}
.center{
    text-align: center;
}
</style>