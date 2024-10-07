# RestV10LinksPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**RestV10LinksPostRequestLink**](RestV10LinksPostRequestLink.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_links_post_request import RestV10LinksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10LinksPostRequest from a JSON string
rest_v10_links_post_request_instance = RestV10LinksPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10LinksPostRequest.to_json())

# convert the object into a dict
rest_v10_links_post_request_dict = rest_v10_links_post_request_instance.to_dict()
# create an instance of RestV10LinksPostRequest from a dict
rest_v10_links_post_request_from_dict = RestV10LinksPostRequest.from_dict(rest_v10_links_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


