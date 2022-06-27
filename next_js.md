# NextJS

### Getting Started
1. 
    - Create Vanilla: `npx create-next-app` 
    - Example Blog: `npx create-next-app --example blog-starter`
    - Initialize Dir as Node Project: `npm init -y`
2. Install `npm install next react react-dom` -> changes in `package.json`, `package-lock.json`
3. `npm run dev`


### Pages

#### Basic:
```js
const Index = () => (
    <div>
        <h1>Home page</h1>
    </div>
)
export default Index
```
#### Linking:
Page destinations defined by script with their script name destination (e.g. `/page2` is defined by `pages/page2.js`)

1. Add `import Link from 'next/link'` to prevent all javascript being fetched for every navigation, and only fetch relevant page
2. Add to be able to query any `/page2/id`
   ```js
   import { useRouter } from 'next/router'
   export default () => {
         const router = useRouter()
         return (
             <>
                 <h1>Blog post</h1>
                     <p>Post id: {router.query.id}</p>
             </>
         )
   }
   ```

### File Manipulation

#### Posts
`import posts from '../../posts.json'`

   
