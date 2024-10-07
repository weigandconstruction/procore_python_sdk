# RestV10CommunicationTagsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_tag** | [**RestV10CommunicationTagsPostRequestCommunicationTag**](RestV10CommunicationTagsPostRequestCommunicationTag.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_communication_tags_post_request import RestV10CommunicationTagsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CommunicationTagsPostRequest from a JSON string
rest_v10_communication_tags_post_request_instance = RestV10CommunicationTagsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CommunicationTagsPostRequest.to_json())

# convert the object into a dict
rest_v10_communication_tags_post_request_dict = rest_v10_communication_tags_post_request_instance.to_dict()
# create an instance of RestV10CommunicationTagsPostRequest from a dict
rest_v10_communication_tags_post_request_from_dict = RestV10CommunicationTagsPostRequest.from_dict(rest_v10_communication_tags_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


