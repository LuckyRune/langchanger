<template>
  <DefaultLayout>
    <div align="right" class="mb10"><a href="/translation"><ButtonBlack value="Переводить"/></a></div>
    <textarea id="read-area" readonly>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem, recusandae consectetur fugit numquam laudantium, 
        hic quaerat dolorem impedit perferendis nam reiciendis? Dicta numquam laboriosam tempora repellendus fuga? Necessitatibus 
        deserunt delectus beatae labore quod maxime ut? Eos natus numquam quas expedita accusamus mollitia dolorum illo! Alias 
        adipisci voluptatem nesciunt numquam enim.
    </textarea>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import ButtonBlack from '@/components/ButtonBlack'

export default {
    name: 'BookReading',
    created () {
      document.title = "Книга1 - Langchanger";
    },

    components: {
        DefaultLayout,
        ButtonBlack
    }
}
</script>

<style scoped>
textarea {
  width: 940px;
  min-width: 940px;
  max-width: 940px;
  height: 75vh;
  min-height: 90px;
  padding: 10px;
}
</style>