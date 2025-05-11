def all_thing_is_obj(object: any) -> int:
        if object is None:
            print(f"The type of the object is indefined")
            return
        print(f"The type of the object is: {type(object)}")
