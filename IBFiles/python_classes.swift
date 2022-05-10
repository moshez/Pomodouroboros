import Foundation

class Actionable: NSObject {
    # Outlets

    # Actions
    @IBAction func doIt(_ sender: NSObject) { }
}

class BigProgressView: NSObject {
    # Outlets

    # Actions
    @IBAction func setLeftColor(_ sender: NSObject) { }
    @IBAction func setRightColor(_ sender: NSObject) { }
}

class DayEditorController: NSObject {
    # Outlets
    @IBOutlet var arrayController: id;
    @IBOutlet var editorWindow: id;
    @IBOutlet var tableView: id;
    # Actions
    @IBAction func hideMe(_ sender: NSObject) { }
}
