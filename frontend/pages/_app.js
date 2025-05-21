import '../src/styles/globals.css';
import Sidebar from '../src/presentation/components/Sidebar';

export default function MyApp({ Component, pageProps }) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Component {...pageProps} />
      </div>
    </div>
  );
}