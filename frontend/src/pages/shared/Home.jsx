import Template from "../../layouts/Template";

export function Home() {
    return (
        <Template>
            <section className="bg-black text-white w-[90%] md:w-[700px] flex-1 m-10 content__landing" >

                <h1 className="text-3xl font-extrabold text-center my-5">
                    Explora, aprende y crece con NeroCrib: <br />
                    Tu aula virtual de diversión <br />
                    inteligente.
                </h1>

                <button className=" login__btn">
                    Inicia sesión
                </button>
             
            </section>
        </Template>
    );
}
