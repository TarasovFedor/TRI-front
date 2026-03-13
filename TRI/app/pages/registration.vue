<template>
    <form class="login">
        <h2 class="login__title">Регистария</h2>
        <div class="login__inputs-box">
            <label class="login__label">
                Имя пользователя
                <input type="text" class="login__input">
            </label>
            <label class="login__label">
                Логин
                <input type="text" class="login__input">
            </label>
            <label  class="login__label">
                Пароль
                <input type="password" class="login__input">
            </label>
        </div>
        <button class="btn login__btn">Зарегистрироваться</button>
        <p class="login__text">
            Еще нет аккаунта? 
            <a href="./login" class="login__link">Войти</a>
        </p>
    </form>
</template>

<script setup>
definePageMeta({
    layout: 'auth',
})

</script>

<style scoped>
.login{
    margin-bottom: 3rem;
}
.login__inputs-box{
    display: flex;
    flex-direction: column;
    margin-bottom: 4.5rem;
    gap: 3rem;
}
.login__label{
    color: var(--color-grey);
    font-size: 1.2rem;
    text-align: start;
}
.login__input{
    width: 100%;
    height: 4rem;
    background-color: #F7F7F7;
    border: none;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    border-radius: .5rem;
}
.login__title{
    font-size: 2.4rem;
    color: var(--color-blue);
    margin-bottom: 6rem;
}
.login__text{
    color: var(--color-grey);
    font-size: 1.4rem;
}
.login__btn{
    font-size: 2rem;
    padding: 1rem 2.3rem;
    text-transform: capitalize;
    margin-bottom: 1.5rem;
}
</style>