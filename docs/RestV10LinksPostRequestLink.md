# RestV10LinksPostRequestLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The user-facing title of the link | 
**url** | **str** | The full URL for the link | 

## Example

```python
from procore_sdk.models.rest_v10_links_post_request_link import RestV10LinksPostRequestLink

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10LinksPostRequestLink from a JSON string
rest_v10_links_post_request_link_instance = RestV10LinksPostRequestLink.from_json(json)
# print the JSON string representation of the object
print(RestV10LinksPostRequestLink.to_json())

# convert the object into a dict
rest_v10_links_post_request_link_dict = rest_v10_links_post_request_link_instance.to_dict()
# create an instance of RestV10LinksPostRequestLink from a dict
rest_v10_links_post_request_link_from_dict = RestV10LinksPostRequestLink.from_dict(rest_v10_links_post_request_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


