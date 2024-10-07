# RestV10CommunicationsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_post** | [**RestV10CommunicationsIdGet200ResponseAllOfInitialPost**](RestV10CommunicationsIdGet200ResponseAllOfInitialPost.md) |  | [optional] 
**communication_tags** | [**List[RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner]**](RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner.md) |  | [optional] 
**created_at** | **date** | Date created | [optional] 
**private** | **bool** | Private flag | [optional] 
**closed** | **bool** | Closed flag | [optional] 
**id** | **int** | ID | [optional] 
**subject** | **str** | Subject | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_communications_id_get200_response import RestV10CommunicationsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CommunicationsIdGet200Response from a JSON string
rest_v10_communications_id_get200_response_instance = RestV10CommunicationsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CommunicationsIdGet200Response.to_json())

# convert the object into a dict
rest_v10_communications_id_get200_response_dict = rest_v10_communications_id_get200_response_instance.to_dict()
# create an instance of RestV10CommunicationsIdGet200Response from a dict
rest_v10_communications_id_get200_response_from_dict = RestV10CommunicationsIdGet200Response.from_dict(rest_v10_communications_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


