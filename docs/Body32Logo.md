# Body32Logo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_uuid** | **str** | UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. | 
**file_name** | **str** | The name of the logo file to be created. | [optional] 

## Example

```python
from procore_sdk.models.body32_logo import Body32Logo

# TODO update the JSON string below
json = "{}"
# create an instance of Body32Logo from a JSON string
body32_logo_instance = Body32Logo.from_json(json)
# print the JSON string representation of the object
print(Body32Logo.to_json())

# convert the object into a dict
body32_logo_dict = body32_logo_instance.to_dict()
# create an instance of Body32Logo from a dict
body32_logo_from_dict = Body32Logo.from_dict(body32_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


