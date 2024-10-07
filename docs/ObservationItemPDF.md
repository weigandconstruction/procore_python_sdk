# ObservationItemPDF


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Observation Item ID | [optional] 
**url** | **str** | URL of PDF file | [optional] 
**pdf_url** | **str** | URL of PDF file | [optional] 

## Example

```python
from procore_sdk.models.observation_item_pdf import ObservationItemPDF

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemPDF from a JSON string
observation_item_pdf_instance = ObservationItemPDF.from_json(json)
# print the JSON string representation of the object
print(ObservationItemPDF.to_json())

# convert the object into a dict
observation_item_pdf_dict = observation_item_pdf_instance.to_dict()
# create an instance of ObservationItemPDF from a dict
observation_item_pdf_from_dict = ObservationItemPDF.from_dict(observation_item_pdf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


