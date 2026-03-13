<template>
        <header>
            <div class="cont header__container">
                <div class="logo">
                    <p class="logo-text">Платформа TRI</p>
                    <button class="btn">Поиск игры</button>
                </div>
                <div class="menu">
                    <button class="btn">Войти</button>
                </div>
            </div>
        </header>

        <main>
            <slot></slot>
        </main>
        <footer class="footer">
            <div class="cont footer__container">
                <div>
                    <h3 class="footer__logo">ТРИ</h3>
                    <p class="footer__desc">Бесплатные текстовые ролевые игры</p>
                </div>
                <div class="material">
                    <h3 class="footer__title">Материалы</h3>
                    <ul class="material__list">
                        <li class="material__item">
                            <a href="#">Правила Сайта</a>
                        </li>
                        <li class="material__item">
                            <a href="#">Как тут играть</a>
                        </li>
                        <li class="material__item">
                            <a href="#">О нарушениях</a>
                        </li>
                        <li class="material__item">
                            <a href="#">Документация</a>
                        </li>
                    </ul>
                </div>
                <div class="networks">
                    <h3 class="footer__title">Соцсети</h3>
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
                                <img src="../icon/footer-networks/Discord.svg" alt="" class="networks__icon">
                            </a>
                        </li>
                    </ul>
                    <p class="netwoks__text">Подписывайтесь на ТРИ в соцсетях, чтобы быть в курсе обновлений.</p>
                </div>
            </div>
        </footer>
        


</template>

<script setup>

</script>

<style scoped>
    .cont{
        width: 1120px;
        margin: 0 auto;
    }
    header{
        padding: 2rem 0;
        box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    }
    .header__container{
        display: flex;
        justify-content: space-between
    }
    .logo{
        display: flex;
        align-items: center;
        gap: 5.3rem;
    }
    .logo-text{
        font-size: 4rem;
        color: #0051A8;
    }

    .footer{
        background-color: var(--color-footer);
        padding: 3rem;
        font-size: 1.2rem;
        color: var(--color-blue);
    }
    .footer__container{
        display: flex;
        justify-content: space-between;
    }
    .footer__title{
        font-size: 2.4rem;
    }
    .footer__logo{
        font-size: 6.4rem;
    }
    .footer__desc{
        font-size: 2rem ;
    }
    .material__list{
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    .networks{
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }
    .networks__list{
        display: flex;
        flex-direction: row;
        gap: 2rem;
    }

</style>