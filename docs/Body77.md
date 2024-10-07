# Body77


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID. Note: Only one of project_id or company_id is required. | 
**developer_app_id** | **str** | ID of an application from the developer portal | 
**notes** | **str** | Notes. Notes to be sent to company admins along with the request. | [optional] 
**implicit** | **bool** | Implicit. Defines whether request has been made implicitly. | 

## Example

```python
from procore_sdk.models.body77 import Body77

# TODO update the JSON string below
json = "{}"
# create an instance of Body77 from a JSON string
body77_instance = Body77.from_json(json)
# print the JSON string representation of the object
print(Body77.to_json())

# convert the object into a dict
body77_dict = body77_instance.to_dict()
# create an instance of Body77 from a dict
body77_from_dict = Body77.from_dict(body77_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


