<template>
    <section class="news">
        <h1 class="news__title">Новостная лента</h1>
        <div class="news__search search">
            <label>
                <input type="text"
                class="search__input"
                placeholder="Поиск">
            </label>
            <div class="news__tags tags">
                <span class="tag">Игры</span>
                <span class="tag">Полки</span>
                <span class="tag">Решение</span>
                <span class="tag">Новости</span>
            </div>
        </div>
        
        <div class="news__post post">
            <div class="post__item">
                <h3 class="post__title">Заголовок новости</h3>
                <p class="post__content">Текст новости...</p>
                <span class="post__date">01.01.2025</span>
            </div>
        </div>
    </section>
</template>

<style scoped>
    .news {
        width: 100%;
        padding: 0 30px;
    }

    .news__title {
        font-size: 24px;
        margin-bottom: 20px;
    }

    .search {
        width: 100%;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 20px;
        background: #f9f9f9;
    }

    .search__input {
        width: 98%;
        border-radius: 8px;
        padding: 8px;
        border: none;
        outline: none;
        border: 1px solid #eee;
        font-size: 16px;
        margin-bottom: 15px;
    }

    .tags {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }

    .tag {
        padding: 6px 12px;
        background: #e9ecef;
        border-radius: 20px;
        font-size: 14px;
        color: #495057;
        cursor: pointer;
        transition: 0.2s;
    }

    .tag:hover {
        background: #dee2e6;
    }

    .post {
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 15px;
        margin-top: 15px;
        background: white;
    }

    .post__title {
        font-size: 18px;
        margin-bottom: 10px;
        color: #2c3e50;
    }

    .post__content {
        color: #555;
        line-height: 1.5;
        margin-bottom: 10px;
    }

    .post__date {
        color: #888;
        font-size: 14px;
    }
</style>