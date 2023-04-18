import {
  CollectionReference,
  collection,
  DocumentData,
} from "firebase/firestore";

export default function () {
  const { firestore } = useFirebase();

  const createCollection = <T = DocumentData>(collectionName: string) => {
    return collection(firestore, collectionName) as CollectionReference<T>;
  };

  const usersCol = createCollection<User>("users");

  return {
    usersCol,
  };
}
