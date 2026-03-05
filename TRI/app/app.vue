<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script>
export default{
  data(){
    return{
      
    }
  }
}
</script>


<style>
/* Normalize */

/**
  Нормализация блочной модели
 */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/**
  Убираем внутренние отступы слева тегам списков,
  у которых есть атрибут class
 */
:where(ul, ol):where([class]) {
  padding-left: 0;
}

/**
  Убираем внешние отступы body и двум другим тегам,
  у которых есть атрибут class
 */
body,
:where(blockquote, figure):where([class]) {
  margin: 0;
}

/**
  Убираем внешние отступы вертикали нужным тегам,
  у которых есть атрибут class
 */
:where(
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  p,
  ul,
  ol,
  dl
):where([class]) {
  margin-block: 0;
  font-weight: 400;
}

:where(dd[class]) {
  margin-left: 0;
}

:where(fieldset[class]) {
  margin-left: 0;
  padding: 0;
  border: none;
}

/**
  Убираем стандартный маркер маркированному списку,
  у которого есть атрибут class
 */
:where(ul[class]) {
  list-style: none;
}

/**
  Обнуляем вертикальные внешние отступы параграфа,
  объявляем локальную переменную для внешнего отступа вниз,
  чтобы избежать взаимодействие с более сложным селектором
 */
p {
  --paragraphMarginBottom: 24px;

  margin-block: 0;
}

/**
  Внешний отступ вниз для параграфа без атрибута class,
  который расположен не последним среди своих соседних элементов
 */
p:where(:not([class]):not(:last-child)) {
  margin-bottom: var(--paragraphMarginBottom);
}


/**
  Упрощаем работу с изображениями
 */
img {
  display: block;
  max-width: 100%;
}

/**
  Наследуем свойства шрифт для полей ввода
 */
input,
textarea,
select,
button {
  font: inherit;
}

html {
  /**
    Пригодится в большинстве ситуаций
    (когда, например, нужно будет "прижать" футер к низу сайта)
   */
  height: 100%;
  /**
    Плавный скролл
   */
  scroll-behavior: smooth;
}

body {
  /**
    Пригодится в большинстве ситуаций
    (когда, например, нужно будет "прижать" футер к низу сайта)
   */
  min-height: 100%;
  /**
    Унифицированный интерлиньяж
   */
  line-height: 1.5;
}

/**
  Приводим к единому цвету svg-элементы
 */
svg *[fill] { fill: currentColor }
svg *[stroke] { stroke: currentColor }

/**
  Чиним баг задержки смены цвета при взаимодействии с svg-элементами
 */
svg * {
  transition-property: fill, stroke;
}

/* Шрифты */
@font-face{
    font-family: 'ABeeZee';
    src: url(../fonts/SpaceGrotesk-Regular.woff2) format('ttf');
    font-weight: 400;
    font-style: normal;
    font-display: swap;
}

/* Variables */

:root{
    --color-blue: #0051A8;
    --color-light: #FFFFFF;
    --color-dark: #000000;
    --color-footer: #E6E9ED;
    --color-grey: #989AA4;

    --border: 1px solid var(--color-dark);

    --font-family-base: 'ABeeZee', sans-serif;
}
html{
  font-size: 62.5%;
  font-family: var(--font-family-base);
}
.cont{
    width: 1120px;
    margin: 0 auto;
}
.btn{
  background-color: #0051A8;
  color: #fff;
  border-radius: .7rem;
  padding: 1.5rem;
  text-transform: uppercase;
  font-size: 1.6rem;
  border: none;
}
</style>