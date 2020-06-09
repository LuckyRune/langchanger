<template>
  <div id="app">
    <Header/>
    <section id="content">
      <div id="wrapper">
          <section id="main">
              <router-view/>
          </section>
          <Footer/>
      </div>
    </section>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
  components: {
    Header,
    Footer
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:400,500&display=swap');

:root {
    /* Элементы */
    --primary: #72ACFF;
    --secondary: #545871;
    --el-background: #F0F1F7;
    --el-holder: rgba(84,88,113,0.6);
    --large-accent: #FA6980;
    /* Текст */
    --text-primary: #000000;
    --text-secondary: #FFFFFF;
    --text-desc: #9597A6;
    --text-link: #00B5AD;
    --text-accent: #72ACFF;
}
::selection {
  background-color: var(--primary);
  color: white;
}
* {
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
    padding: 0;
    margin: 0;
    outline: none;
}

/* Заголовки */
h1 {
  font-size: 54px;
}
h2 {
  font-size: 36px;
}
h3 {
  font-size: 24px;
  color: var(--text-accent);
}
h4 {
  font-size: 20px;
}
h5 {
  font-size: 18px;
  color: var(--text-accent);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 10px;
}
/* Параграфы */
p {
  font-size: 18px;
}
/* Ссылки */
a {
  text-decoration: none;
}
/* Textarea */
.origin-read-frame, textarea {
  border: 0;
  border-radius: 6px;
  font-size: 16px;
  min-height: 20px;
  box-shadow: 0 0 2px black;
}

textarea {
  padding: 5px;
}

/* Отступы */
.mt5 {
  margin-top: 5px;
}

.mt20 {
  margin-top: 20px;
}

.ml20 {
  margin-left: 20px;
}

.mb5 {
  margin-bottom: 5px;
}
.mb10 {
  margin-bottom: 10px;
}
.mb20 {
  margin-bottom: 20px;
}
.mb40 {
  margin-bottom: 40px;
}

.mr5 {
  margin-right: 5px;
}
.mr10 {
  margin-right: 10px;
}
.mr20 {
  margin-right: 20px;
}
.mr40 {
  margin-right: 40px;
}
/* Стиль форм */
.form-style h2 {
  color: var(--text-accent);
}

.form-style a {
  color: var(--text-link);
}

.form-style a:hover {
  text-decoration: underline;
}

.form-style input {
  padding: 0 5px;
  border: 0;
  border-radius: 6px;
  width: 430px;
  height: 30px;
  font-size: 16px;
  box-shadow: 0 0 2px black;
}

.form-style textarea {
  width: 430px;
  height: 90px;
  min-width: 430px;
  max-width: 430px;
  min-height: 90px;
}

.form-style input:focus {
  box-shadow: 0 0 4px black;
}
/* Стиль SVG placeholders */
.svg-placeholder {
  border: 2px solid var(--el-holder);
  border-radius: 6px;
  background-color: var(--el-background);
  display: flex;
  justify-content: center;
  align-items: center;
}
/*.svg-placeholder img {
  width: 50%;
  height: 50%;
} */

#main {
  padding: 50px 20px 40px 20px;
}

#content {
  display: flex;
  align-items: center;
  flex-direction: column;
}

#wrapper {
  margin-top: -10px;
  z-index: 0;
  box-shadow: 0 0 7px black;
}

#wrapper, footer {
  width: 1000px;
}

select {
  width: 150px;
  height: 40px;
  font-size: 16px;
  box-shadow: 0 0 2px black;
  border-radius: 6px;
  margin-right: 10px;
}

select:hover {
  box-shadow: 0 0 4px black;
}

.btnBlack {
  min-width: 150px;
  height: 40px;
  padding: 0 10px;
  font-size: 18px;
  text-transform: uppercase;
  border: 0;
  border-radius: 4px;
  background-color: var(--secondary);
  color: white;
}

.btnBlack:hover {
  box-shadow: 0 0 3px black;
  cursor: pointer;
}

.btnBlack:active {
  background-color: white;
  color: var(--secondary);
  border: 1px solid var(--secondary);
  box-shadow: 0 0 3px black inset;
}

.btnBlack:disabled {
  background-color: gray;
}

.btnBlack:disabled:hover {
  box-shadow: none;
  cursor: default;
}

.btnDelete {
  background-color: var(--large-accent);
  padding: 6px 8px;
  border-radius: 3px;
  color: white;
  border: 0;
  margin-left: 5px;
}

.btnDelete:hover {
  box-shadow: 0 0 2px black;
  cursor: pointer;
}

.invalid-feedback {
  margin-top: 5px;
  color: var(--large-accent);
  max-width: 440px;
}
</style>
