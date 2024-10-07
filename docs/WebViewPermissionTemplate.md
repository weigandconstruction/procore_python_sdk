# WebViewPermissionTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Permission Template | [optional] 
**name** | **str** | The name of the Permission Template | [optional] 

## Example

```python
from procore_sdk.models.web_view_permission_template import WebViewPermissionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WebViewPermissionTemplate from a JSON string
web_view_permission_template_instance = WebViewPermissionTemplate.from_json(json)
# print the JSON string representation of the object
print(WebViewPermissionTemplate.to_json())

# convert the object into a dict
web_view_permission_template_dict = web_view_permission_template_instance.to_dict()
# create an instance of WebViewPermissionTemplate from a dict
web_view_permission_template_from_dict = WebViewPermissionTemplate.from_dict(web_view_permission_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


