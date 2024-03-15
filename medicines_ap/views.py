from medicines_ap.librariess import *

#database for medicine and connectivity with mongodb 

class MedicineAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self , request):
        data = request.data #here in data all the medicine data will come
        serializer = MedicineSerializer(data = data)
        if not serializer.is_valid(): #firstly it will check for validation here
            return Response({"errors": serializer.errors ,"message":"something went wrong" }, status=status.HTTP_400_BAD_REQUEST) #if error accurs it will give error
        collection.insert_one(data)
        return Response({"message":"your data is saved successfully"}, status=status.HTTP_201_CREATED )#if valid then give this response
    
    def get(self , request , _id=None):
        if _id == None:
            medicine_data = collection.find()# here in medicine_data i am storing all the data of database of medicine
            json_data =  json.loads(json_util.dumps(medicine_data)) # in json_data  i am storing our medicine data into json format
            return JsonResponse(json_data , safe=False , status=status.HTTP_200_OK)
        id = ObjectId(_id) 
        medicine_data = collection.find_one({"_id" : id}) #here in medicine_data  i am storing the data of single record of particular id
        json_data =  json.loads(json_util.dumps(medicine_data)) #here in json_data  i am converting MongoDB documents into  a JSON-serializable format
        if not json_data:  #if no data is present then it will give error
            return Response({"message":" sorry data is not present" }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(json_data , safe=False , status=status.HTTP_200_OK) #returning the response of the api will full data of medicine

 
    def put(self, request, _id):
        id=ObjectId(_id) # here in id i an taking the id of which data we want , so for that i have converted the id into object id
        prev_data = collection.find_one({"_id": id}) #here in prev_data  previous data of that particular id will store and come 
        if not prev_data:
            return Response({"message": "Data with the given ID not found"}, status=status.HTTP_404_NOT_FOUND) #if not then will give error

        new_data = {"$set": request.data} #here in new_data  we are storing the updated data which user want to update

        collection.update_one({"_id": id}, new_data) #here new_data that  you want to update into the database will come and on the based of id it will update

        return Response({"data": request.data, 'message': 'Your Medicine data is updated successfully 🎊'}, status=status.HTTP_200_OK) #if all things goes well data will update


    def delete(self , request , _id):
        id = ObjectId(_id)
        data = collection.find_one({"_id" : id}) #here in data  we are getting the specific data which user wants to delete
        if not data: #checking whether data is there or not
            context = {"message" : "data is not present"} 
            return Response(context , status=status.HTTP_404_NOT_FOUND )
        collection.delete_one({"_id" : id})
        return Response({"message" : "data deleted successfully"} , status=status.HTTP_200_OK) # if will things well then will delete the data
    
    
 
# database for customer and connectivity with postgresql Customer_data

class CustomerAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data #here data will come 
        serializer=Customer_dataSerializer(data=data)
        if not serializer.is_valid():#if the data which we are sending is valid or not then it will return error
 
            print(serializer.errors)
            return Response({'status':403,'erorors':serializer.errors,'message':'something went wrong'})
            
        serializer.save()
       
        return Response({'status':200,'payload':serializer.data,'message':'your data is saved successfully'}) 
    
    def put(self, request, id):
        # Get the existing instance by ID
        try:
            data_customer = Customer_data.objects.get(id=id)
        except Customer_data.DoesNotExist: #here it will throw an exception if error come
            return Response({"message": "Data with the given ID not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Customer_dataSerializer(data_customer, data=request.data, partial=True)
        
        if serializer.is_valid(): # if Validate then save the serializer
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": serializer.errors}) #here error will thrown

    def delete(self, request, id):
      
        try:
            data_id = Customer_data.objects.get(id=id)
        except Customer_data.DoesNotExist:#here it will throw an exception if error come
            return Response({"message": "Data with the given ID not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Customer_dataSerializer(data_id)
        data_id.delete() #if all things goes well then will delete data on the based particular id
        return Response({"message": "Data is deleted"}, status=status.HTTP_200_OK)
    
    
    def get(self, request, id=None): #here the  function of getting id and if id will be  none then we have to send response for list of data 
       #otherwise if id is specified then it will fetch the data of particular id
        if id is not None:
            try:
                object_id_one = Customer_data.objects.get(id=id) # here in object_id_one  we are storing one data which is fetch from the db

                serializer = Customer_dataSerializer(object_id_one)

                return Response({"data": serializer.data})
            
            except Customer_data.DoesNotExist:#if id doesnt match then will throw an exception

                return Response({"message": "Data with the given ID not found"}, status=status.HTTP_404_NOT_FOUND)

        else:
            object_all_data = Customer_data.objects.all()# If ID is not provided, fetch all objects
            serializer = Customer_dataSerializer(object_all_data, many=True)
            return Response({"data": serializer.data}) 
    

    
