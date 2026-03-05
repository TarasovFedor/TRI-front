<template>
    <section>
        <div class="cont auth">
            <h1 class="auth__title">Добро пожаловать!</h1>
            
            <slot></slot>

            
            <div class="auth__line"></div>
            <p class="auth__text">Войти с помощью:</p>
            <div class="auth__icon-container">
                <a href="#" class="icons__link">
                    <img src="../icon/auth/mail.svg" alt="">
                </a>
                <a href="#" class="icons__link">
                    <img src="../icon/auth/vk.svg" alt="">
                </a>
                <a href="#" class="icons__link">
                    <img src="../icon/auth/google.svg" alt="">
                </a>
            </div>
        </div>
    </section>
</template>

<style scoped>
.auth{
    padding-block: 3rem;
    text-align: center;
    max-width: 55rem;
}
.auth__title{
    color: var(--color-blue);
    font-size: 3.2rem;
}
.auth__line{
    border-bottom: 1px solid var(--color-blue);
    margin: 0 auto;
    margin-bottom: 1rem;
}
.auth__text{
    font-size: 1.3rem;
    color: var(--color-blue);
    margin-bottom: 1rem;
}
.auth__icon-container{
    display: flex;
    gap: 2rem;
    align-items: center;
    justify-content: center;
}
</style>