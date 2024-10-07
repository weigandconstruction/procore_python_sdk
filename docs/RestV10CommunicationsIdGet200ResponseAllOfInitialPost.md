# RestV10CommunicationsIdGet200ResponseAllOfInitialPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**subject** | **str** | Subject | [optional] 
**email_sent_at** | **datetime** | Date email sent | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_communications_id_get200_response_all_of_initial_post import RestV10CommunicationsIdGet200ResponseAllOfInitialPost

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CommunicationsIdGet200ResponseAllOfInitialPost from a JSON string
rest_v10_communications_id_get200_response_all_of_initial_post_instance = RestV10CommunicationsIdGet200ResponseAllOfInitialPost.from_json(json)
# print the JSON string representation of the object
print(RestV10CommunicationsIdGet200ResponseAllOfInitialPost.to_json())

# convert the object into a dict
rest_v10_communications_id_get200_response_all_of_initial_post_dict = rest_v10_communications_id_get200_response_all_of_initial_post_instance.to_dict()
# create an instance of RestV10CommunicationsIdGet200ResponseAllOfInitialPost from a dict
rest_v10_communications_id_get200_response_all_of_initial_post_from_dict = RestV10CommunicationsIdGet200ResponseAllOfInitialPost.from_dict(rest_v10_communications_id_get200_response_all_of_initial_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


